import 'package:clean_architecure_demo/domain/entities/barber.dart';
import 'package:clean_architecure_demo/domain/repositories/barber_repository.dart';

class GetBarbersByIdUseCase {
  final BarberRepository barberRepository;

  GetBarbersByIdUseCase(this.barberRepository);

  Future<Barber> call(String id) async {
    return await barberRepository.getBarberById(id);
  }
}
