import '../entities/barber.dart';
import '../repositories/barber_repository.dart';

class GetBarbersUseCase {
  final BarberRepository repository;

  GetBarbersUseCase(this.repository);

  Future<List<Barber>> call() {
    return repository.getBarbers();
  }
}
