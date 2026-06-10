import '../../domain/entities/barber.dart';
import '../../domain/repositories/barber_repository.dart';
import '../sources/barber_remote_source.dart';

class BarberRepositoryImpl implements BarberRepository {
  final BarberRemoteSource remoteSource;

  BarberRepositoryImpl(this.remoteSource);

  @override
  Future<List<Barber>> getBarbers() async {
    final models = await remoteSource.getBarbers();
    return models;
  }

  @override
  Future<Barber> getBarberById(String id) async {
    final model = await remoteSource.getBarberById(id);
    return model;
  }
}
