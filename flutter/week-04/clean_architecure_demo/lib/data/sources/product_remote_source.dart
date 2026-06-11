import '../models/product_model.dart';

class ProductRemoteSource {
  // In real demo — this would use Dio to call an API
  // For now — fake data simulating an API response

  Future<List<ProductModel>> getProducts() async {
    await Future.delayed(Duration(seconds: 1)); // simulate network delay

    final fakeResponse = [
      {
        'id': '1',
        'name': 'Laptop Pro',
        'price': 'USD 999.99',
        'is_active': true,
        'quantity': 45,
      },
      {
        'id': '2',
        'name': 'Wireless Mouse',
        'price': 'USD 29.99',
        'is_active': true,
        'quantity': 120,
      },
      {
        'id': '3',
        'name': 'USB-C Cable',
        'price': 'USD 15.99',
        'is_active': false,
        'quantity': 200,
      },
    ];

    return fakeResponse.map((json) => ProductModel.fromJson(json)).toList();
  }

  Future<ProductModel> getProductById(String id) async {
    await Future.delayed(Duration(milliseconds: 500));

    final products = await getProducts();
    return products.firstWhere((p) => p.id == id);
  }
}
