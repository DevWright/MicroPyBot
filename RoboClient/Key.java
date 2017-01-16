
// import engine.game.GameInfo;

//Key must know whether it was just pressed, or just released for each game update.
public class Key {
	private boolean isDown;
	private boolean wasDownPressTest;
	private boolean wasDownReleaseTest;
	private int lastFramePressed = -1;
	private int lastFrameReleased = -1;
	
	public boolean testIfDown() {
		return isDown;
	}
	
	// public boolean testIfPressed() {
	// 	if (isDown && !wasDownPressTest) {
	// 		wasDownPressTest = true;
	// 		lastFramePressed = GameInfo.gameFrameNumber;
	// 		return true;
	// 	} else if (GameInfo.gameFrameNumber == lastFramePressed) {
	// 		return true;
	// 	} else if (!isDown) {
	// 		wasDownPressTest = false;
	// 		return false;
	// 	} else {
	// 		return false;
	// 	}
	// }
	
	// public boolean testIfReleased() {
	// 	if (!isDown && wasDownReleaseTest) {
	// 		wasDownReleaseTest = false;
	// 		lastFrameReleased = GameInfo.gameFrameNumber;
	// 		return true;
	// 	} else if (GameInfo.gameFrameNumber == lastFrameReleased) {
	// 		return true;
	// 	} else if (isDown) {
	// 		wasDownReleaseTest = true;
	// 		return false;
	// 	} else {
	// 		return false;
	// 	}
	// }
	
	public void press() {
//		if (!isDown) {
			isDown = true;
//			lastFramePressed = GameInfo.gameFrameNumber;
//		}
	}
	
	public void release() {
//		if (isDown) {
			isDown = false;
//			lastFrameReleased = GameInfo.gameFrameNumber;
//		}
	}

}
