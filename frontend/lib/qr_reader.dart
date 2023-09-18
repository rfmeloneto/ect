import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:qr_bar_code_scanner_dialog/qr_bar_code_scanner_dialog.dart';

class QrCodeReader extends StatefulWidget {
  const QrCodeReader({super.key});

  @override
  State<QrCodeReader> createState() => _QrCodeReaderState();
}

class _QrCodeReaderState extends State<QrCodeReader> {
  final _qrBarCodeScannerDialogPlugin = QrBarCodeScannerDialog();
  String qrData = '';
  String confirmationMessage = '';

  Map<String, dynamic> parseQRData(String data) {
    List<String> parts = data.split(' ');

    Map<String, dynamic> jsonData = {};

    for (String part in parts) {
      List<String> keyValue = part.split(':');

      if (keyValue.length == 2) {
        String chave = keyValue[0].trim().toString();
        String valor = keyValue[1].trim().toString();

        jsonData[chave] = valor;
      }
    }

    return jsonData;
  }

  void postJsonData(parsedData) async {
    Dio dio = Dio();
    String url = 'http://10.113.254.27:8002/eleicao/api/salvar_urna/';
    //String url = 'http://localhost:8002/eleicao/api/salvar_urna/';
    print("############## ENTROU NA COMUNICAÇÃO ##############");
    try {
      print("############## ENTROU NO TRY ##############");
      Response response = await dio.post(
        url,
        data: parsedData,
        options: Options(headers: {
          'Content-Type': 'application/json',
        }),
      );
      if (response.statusCode == 200) {
        confirmationMessage = 'Enviado com sucesso!';
        print("Enviado com sucesso!");
      } else {
        confirmationMessage = 'Erro na requisição: ${response.statusCode}';
        print("Erro na requisição: ${response.statusCode}");
      }
    } catch (e) {
      confirmationMessage = e.toString();
      print("############## ENTROU NO ERRO ##############");
      print("Erro: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Leitor de Boletim Urna'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              if (confirmationMessage != '')
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text(confirmationMessage),
                ),
              if (qrData != '')
                Padding(
                  padding: const EdgeInsets.all(8.0),
                  child: Text('Boletim Urna: $qrData'),
                ),
              SizedBox(
                width: 300,
                height: 100,
                child: ElevatedButton.icon(
                  icon: const Icon(Icons.qr_code_scanner),
                  onPressed: () {
                    _qrBarCodeScannerDialogPlugin.getScannedQrBarCode(
                        context: context,
                        onCode: (qrData) {
                          setState(() {
                            this.qrData = qrData!;
                            final parsedData = parseQRData(qrData);
                            postJsonData(parsedData);
                            print(parsedData);
                          });
                        });
                  },
                  label: const Text("Ler Boletim de Urna"),
                ),
              ),
            ],
          ),
        ));
  }
}
