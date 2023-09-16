import 'dart:io';
import 'dart:convert';

import 'package:dio/dio.dart';
import 'package:flutter/material.dart';
import 'package:qr_code_scanner/qr_code_scanner.dart';
import 'package:http/http.dart' as http;

class QRCodeScannerApp extends StatefulWidget {
  const QRCodeScannerApp({super.key});

  @override
  _QRCodeScannerAppState createState() => _QRCodeScannerAppState();
}

class _QRCodeScannerAppState extends State<QRCodeScannerApp> {
  final GlobalKey qrKey = GlobalKey(debugLabel: 'QR');
  QRViewController? controller;
  String confirmationMessage = '';
  @override
  void reassemble() {
    super.reassemble();
    if (Platform.isAndroid) {
      controller!.pauseCamera();
    } else if (Platform.isIOS) {
      controller!.resumeCamera();
    }
  }

  @override
  void dispose() {
    controller?.dispose();
    super.dispose();
  }

  void _onQRViewCreated(QRViewController controller) {
    this.controller = controller;
    controller.scannedDataStream.listen((scanData) {
      processScannedData(scanData.code!);
    });
  }

  Future<void> processScannedData(String data) async {
    try {
      Map<String, dynamic> jsonData = parseQRData(data);

      final response = await sendJsonDataToServer(jsonData);

      if (response.statusCode == 200) {
        setState(() {
          confirmationMessage = 'Enviado com sucesso!';
        });
      } else {
        setState(() {
          confirmationMessage = 'Erro ao enviar os dados.';
        });
      }
    } catch (e) {
      setState(() {
        confirmationMessage = e.toString();
      });
    }
  }

  Future<http.Response> sendJsonDataToServer(
      Map<String, dynamic> jsonData) async {
    final response = await http.post(
      Uri.parse('http://10.113.254.27:8002/eleicao/api/salvar_urna/'),
      headers: <String, String>{'Content-Type': 'application/json'},
      body: jsonEncode(jsonData),
    );
    return response;
  }

  Map<String, dynamic> parseQRData(String data) {
    List<String> parts = data.split(' ');

    Map<String, dynamic> jsonData = {};

    for (String part in parts) {
      List<String> keyValue = part.split(':');

      if (keyValue.length == 2) {
        String chave = keyValue[0].trim();
        String valor = keyValue[1].trim();

        jsonData[chave] = valor;
      }
    }

    return jsonData;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Leitor de Boletim Urna'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            Expanded(
              flex: 5,
              child: QRView(
                key: qrKey,
                onQRViewCreated: _onQRViewCreated,
              ),
            ),
            Expanded(
              flex: 1,
              child: Center(
                child: Text(confirmationMessage),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
