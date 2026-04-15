import 'package:dio/dio.dart';

class ApiClient {
  late final Dio _dio;

  ApiClient() {
    _dio = Dio(
      BaseOptions(
        baseUrl: 'https://api.cutabove.com',
        connectTimeout: Duration(seconds: 5),
        sendTimeout: Duration(seconds: 5),
        receiveTimeout: Duration(seconds: 10),
      ),
    );

    _setupInterceptors();
  }

  void _setupInterceptors() {
    _dio.interceptors.add(
      InterceptorsWrapper(
        onRequest: (options, handler) {
          print('REQUEST: ${options.method} ${options.path}');
          options.headers['Authorization'] = 'Bearer your_token_here';
          handler.next(options);
        },
        onResponse: (response, handler) {
          print(
            'RESPONSE: ${response.statusCode} ${response.requestOptions.path}',
          );
          handler.next(response);
        },
        onError: (error, handler) {
          print('ERROR: ${error.message}');
          handler.next(error);
        },
      ),
    );
  }
}
