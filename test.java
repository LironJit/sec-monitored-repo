import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Calculator extends Remote {
    Object calculate(Object request) throws RemoteException;
}
