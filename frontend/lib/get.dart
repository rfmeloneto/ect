import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

class get_value extends StatefulWidget {
  const get_value({super.key});

  @override
  State<get_value> createState() => _get_valueState();
}

Future<dynamic> getData() async {
  Response response =
      await Dio().get('http://10.113.254.27:8002/eleicao/api/listar_votos/');
  print(response.data);
  return response.data;
}

class _get_valueState extends State<get_value> {
  @override
  Widget build(BuildContext context) {
    getData();
    return const Placeholder();
  }
}
