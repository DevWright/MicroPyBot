
import java.util.HashMap;

import javafx.event.EventHandler;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;

public class KeypressManager implements EventHandler<KeyEvent> {
	private static HashMap<KeyCode, Key> keyPressedMap = new HashMap<>();
	
	public KeypressManager() {
		for (KeyCode k : KeyCode.values()) {
			keyPressedMap.put(k, new Key());
		}
	}

	@Override
	public void handle(KeyEvent event) {
		Key key = keyPressedMap.get(event.getCode());
		
		if (event.getEventType() == KeyEvent.KEY_PRESSED) {
			key.press();
		} else if (event.getEventType() == KeyEvent.KEY_RELEASED) {
			key.release();
		}
	}
	

	public static boolean isKeyDown(KeyCode code) {
		Key key = keyPressedMap.get(code);
		return key.testIfDown();
	}
	
	// public static boolean wasKeyPressed(KeyCode code) {
	// 	Key key = keyPressedMap.get(code);
	// 	return key.testIfPressed();
	// }
	
	// public static boolean wasKeyReleased(KeyCode code) {
	// 	Key key = keyPressedMap.get(code);
	// 	return key.testIfReleased();
	// }
}
