import 'package:clean_architecure_demo/domain/entities/product.dart';
import 'package:clean_architecure_demo/domain/repositories/product_repository.dart';

class GetProductsByIdUseCase {
  final ProductRepository productRepository;

  GetProductsByIdUseCase(this.productRepository);

  Future<Product> call(String id) async {
    return await productRepository.getProductById(id);
  }
}
