import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../data/repositories/barber_repository_impl.dart';
import '../../data/sources/barber_remote_source.dart';
import '../../domain/entities/barber.dart';
import '../../domain/usecases/get_barbers_usecase.dart';

// What the UI needs — list of barbers
final barbersProvider = FutureProvider<List<Barber>>((ref) {
  final useCase = ref.watch(getBarbersUseCaseProvider);
  return useCase();
});

// What barbersProvider needs — the use case
final getBarbersUseCaseProvider = Provider<GetBarbersUseCase>((ref) {
  final repository = ref.watch(barberRepositoryProvider);
  return GetBarbersUseCase(repository);
});

// What the use case needs — the repository implementation
final barberRepositoryProvider = Provider<BarberRepositoryImpl>((ref) {
  final remoteSource = ref.watch(barberRemoteSourceProvider);
  return BarberRepositoryImpl(remoteSource);
});

// What the repository needs — the data source
final barberRemoteSourceProvider = Provider<BarberRemoteSource>((ref) {
  return BarberRemoteSource();
});
