import '../../domain/entities/product.dart';
import '../../domain/repositories/product_repository.dart';
import '../sources/product_remote_source.dart';

class ProductRepositoryImpl implements ProductRepository {
  final ProductRemoteSource remoteSource;

  ProductRepositoryImpl(this.remoteSource);

  @override
  Future<List<Product>> getProducts() async {
    final models = await remoteSource.getProducts();
    return models;
  }

  @override
  Future<Product> getProductById(String id) async {
    final model = await remoteSource.getProductById(id);
    return model;
  }
}
