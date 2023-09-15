import 'package:flutter/material.dart';
import 'package:qr_code_scanner/qr_code_scanner.dart';
import 'package:http/http.dart' as http;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: QRCodeScannerApp(),
    );
  }
}

class QRCodeScannerApp extends StatefulWidget {
  const QRCodeScannerApp({super.key});

  @override
  QRCodeScannerAppState createState() => QRCodeScannerAppState();
}

class QRCodeScannerAppState extends State<QRCodeScannerApp> {
  final GlobalKey qrKey = GlobalKey(debugLabel: 'QR');
  QRViewController? controller;
  String confirmationMessage = '';

  @override
  void dispose() {
    controller?.dispose();
    super.dispose();
  }

  void _onQRViewCreated(QRViewController controller) {
    this.controller = controller;
    controller.scannedDataStream.listen((scanData) {
      // Parse and process the scanned data
      processScannedData(scanData.code);
    });
  }

  void processScannedData(String data) async {
    try {
      // Parse the scanned data and create a JSON object
      Map<String, dynamic> jsonData = parseQRData(data);

      // Send the JSON data to the server
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/eleicao/api/salvar_urna/'),
        headers: <String, String>{'Content-Type': 'application/json'},
        body: jsonData,
      );

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
        confirmationMessage = 'Erro ao processar os dados QR.';
      });
    }
  }

  Map<String, dynamic> parseQRData(String data) {
    // Implemente a lógica para analisar os dados QR e criar um mapa JSON.
    // Certifique-se de converter os valores relevantes para inteiros.
    // Você pode usar a função split para dividir os valores e parseInt para converter em inteiros.
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Leitor de Código QR'),
      ),
      body: Center(
        child: Column(
          children: <Widget>[
            Expanded(
              flex: 4,
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
