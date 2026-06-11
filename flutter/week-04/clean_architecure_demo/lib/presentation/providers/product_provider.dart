import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../data/repositories/product_repository_impl.dart';
import '../../data/sources/product_remote_source.dart';
import '../../domain/entities/product.dart';
import '../../domain/usecases/get_products_usecase.dart';

// What the UI needs — list of products
final productsProvider = FutureProvider<List<Product>>((ref) {
  final useCase = ref.watch(getProductsUseCaseProvider);
  return useCase();
});

// What productsProvider needs — the use case
final getProductsUseCaseProvider = Provider<GetProductsUseCase>((ref) {
  final repository = ref.watch(productRepositoryProvider);
  return GetProductsUseCase(repository);
});

// What the use case needs — the repository implementation
final productRepositoryProvider = Provider<ProductRepositoryImpl>((ref) {
  final remoteSource = ref.watch(productRemoteSourceProvider);
  return ProductRepositoryImpl(remoteSource);
});

// What the repository needs — the data source
final productRemoteSourceProvider = Provider<ProductRemoteSource>((ref) {
  return ProductRemoteSource();
});
