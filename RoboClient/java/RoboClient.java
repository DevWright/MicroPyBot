import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.DatagramPacket;

import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.event.EventHandler;
import javafx.stage.WindowEvent;
import javafx.scene.input.KeyCode;

public class RoboClient {
	private static boolean guiInitialized = false;
	private static boolean running = true;

	private static final String SERVER_ADDRESS = "192.168.4.1";
	private static final int SERVER_PORT = 6563;
	private static final int SEND_FREQUENCY = 30;
	private static final int MAX_POWER = 1023;



	public static class GuiBuilder extends Application implements Runnable {

		@Override
		public void start(Stage primaryStage) throws Exception {
			primaryStage.setTitle("RoboClient");

			Label label = new Label("Press arrow keys to send commands");
			Scene scene = new Scene(label, 400, 200);

			KeypressManager km = new KeypressManager();
			scene.setOnKeyPressed(km);
			scene.setOnKeyReleased(km);
			scene.setOnKeyTyped(km);

			primaryStage.setScene(scene);

			primaryStage.show();

			primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
				public void handle(WindowEvent we) {
					System.out.println("Exiting RoboClient...");
					running = false;
				}
			});

			guiInitialized = true;
		}

		@Override
		public void run() {
			launch();
		}

	}



	public static void main(String[] args) throws Exception {
		Thread t = new Thread(new GuiBuilder());
		t.start();

		while(!guiInitialized) {
			Thread.sleep(10);
		}

		sendCommands(SERVER_ADDRESS, SERVER_PORT);
	}


	private static void sendCommands(String host, int port) throws Exception {
		DatagramSocket socket = new DatagramSocket();
		InetAddress address = InetAddress.getByName(host);

		int delay = 1000 / SEND_FREQUENCY;

		while (running) {

			boolean upPressed = KeypressManager.isKeyDown(KeyCode.UP);
			boolean downPressed = KeypressManager.isKeyDown(KeyCode.DOWN);
			boolean leftPressed = KeypressManager.isKeyDown(KeyCode.LEFT);
			boolean rightPressed = KeypressManager.isKeyDown(KeyCode.RIGHT);

			int speed = 0;
			if (upPressed) {
				speed += MAX_POWER;
			}

			if (downPressed) {
				speed -= MAX_POWER;
			}

			int turn = 0;
			if (rightPressed) {
				turn += MAX_POWER;
			}

			if (leftPressed) {
				turn -= MAX_POWER;
			}

			String data = speed + ":" + turn;

			System.out.println("Sending current data: " + data);

			byte[] message = data.getBytes();

			DatagramPacket packet = new DatagramPacket(message, message.length, address, SERVER_PORT);

			socket.send(packet);

			Thread.sleep(delay);
		}
	}
}