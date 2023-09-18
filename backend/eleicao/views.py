import json

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Candidatos, Cidades, Estado, Urnas, ProcessoEleitoral
from .serializer import (CandidatoSerializer, CidadeSerializer,
                         EstadoSerializer, UrnaSerializer)


class UrnaAPI(APIView):
    def post(self, request, format=None):
        try:
            data = request.data

            urna_data = {
                'vqr': data['VRQR'],
                'vrch': data['VRCH'],
                'orig': data['ORIG'],
                'orlc': data['ORLC'],
                'proc': data['PROC'],
                'dtpl': data['DTPL'],
                'plei': data['PLEI'],
                'turn': data['TURN'],
                'fase': data['FASE'],
                'zona': data['ZONA'],
                'seca': data['SECA'],
                'idue': data['IDUE'],
                'idca': data['IDCA'],
                'loca': data['LOCA'],
                'apto': data['APTO'],
                'comp': data['COMP'],
                'falt': data['FALT'],
                'datab': data['DTAB'],
                'hrab': data['HRAB'],
                'dtfc': data['DTFC'],
                'hrfc': data['HRFC'],
                'idel': data['IDEL'],
                'carg': data['CARG'],
                'tipo': data['TIPO'],
                'verc': data['VERC'],
                'apta': data['APTA'],
                'nomi': data['NOMI'],
                'bran': data['BRAN'],
                'nulo': data['NULO'],
                'totc': data['TOTC'],
                'hash': data['HASH'],
                'assi': data['ASSI'],
            }

            cidade_data = {
                'muni': data['MUNI'],
            }

            estado_data = {
                'unfe': data['UNFE'],
            }

            candidato_data = {key: value for key,
                              value in data.items() if key.isdigit()}
            print(candidato_data)
            # or ~Q(ProcessoEleitoral.objects.filter(numero=urna_data['plei']).exists()
            urna_serializer = UrnaSerializer(data=urna_data)
            processo = ProcessoEleitoral.objects.get(
                numero=urna_data['plei'])
            if processo.is_valid is False or processo is None:
                return Response({"error": "Processo eleitoral Não Existe ou não está ativo."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if Urnas.objects.filter(hash=urna_data['hash'], assi=urna_data['assi']).exists():
                    return Response({"error": "Urna já cadastrada."}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    if urna_serializer.is_valid():
                        urna_data = urna_serializer.validated_data
                        urna_data['processo_eleitoral'] = processo
                        urna = urna_serializer.save()

                        cidade_serializer = CidadeSerializer(data=cidade_data)
                        if cidade_serializer.is_valid():
                            if Cidades.objects.filter(muni=cidade_data['muni']).exists():
                                cidade = Cidades.objects.get(
                                    muni=cidade_data['muni'])
                                cidade.urna.add(urna)
                            else:
                                cidade = cidade_serializer.save()
                                cidade.urna.add(urna)

                            estado_serializer = EstadoSerializer(
                                data=estado_data)
                            if estado_serializer.is_valid():
                                if Estado.objects.filter(unfe=estado_data['unfe']).exists():
                                    estado = Estado.objects.get(
                                        unfe=estado_data['unfe'])
                                    estado.cidade.add(cidade)
                                else:
                                    estado = estado_serializer.save()
                                    estado.cidade.add(cidade)

                                for candidato_numero, quantidade_votos in candidato_data.items():
                                    candidato_serializer = CandidatoSerializer(data={
                                        'numero_candidato': candidato_numero,
                                        'votos': quantidade_votos
                                    })
                                    if candidato_serializer.is_valid():
                                        candidato = candidato_serializer.save()
                                        urna.candidato.add(candidato)
                                    else:
                                        return Response(candidato_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                return Response({"message": "Dados salvos com sucesso."}, status=status.HTTP_201_CREATED)
                            else:
                                return Response(estado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response(cidade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(urna_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Trate quaisquer exceções que possam ocorrer durante o processo de salvamento
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CandidatoListView(ListAPIView):
    queryset = Candidatos.objects.all()
    serializer_class = CandidatoSerializer
