class Main:

"""
Time to build the model. For this example Ill build 3 states
"""

    def ModelBuild(self):
         self._model = Model(3, self)
        
        self._timer.Setatzero()
        self._LiftingMechanism.lowestpoint()
        
        # Transitions
        self._model.addTransition(0, TIMEOUT, 1)
        self._model.addTransition(1, TIMEOUT, 2)
        self._model.addTransition(2, TIMEOUT, 3)

    """
   Entry actions for each state
    """
    def stateEntered(self, stateno):
        if stateno == 0:        # State 0 Entry Act
            self._DCMotors.off()
            self._BarcodeReader.off()
            self._Lights.off()
            self._InfraredSensor.off()
            self._Touch-SensitiveBumper.off()
            self._Battery.off()
            self._Clock.Active()
            self._display.showText("0: Unit will turn on at 7:00 A.M")
        elif stateno == 1:      # State 1 Entry Act
            self._DCMotors.on()
            self._BarcodeReader.on()
            self._Lights.on()
            self._InfraredSensor.on()
            self._Touch-SensitiveBumper.on()
            self._Battery.on()
            self._Clock.Active()
            self._display.showText("1: Unit Ready")
        elif stateno == 2:      # State 2 Entry Act
            self._DCMotors.on()
            self._BarcodeReader.on()
            self._Lights.on()
            self._InfraredSensor.on()
            self._Touch-SensitiveBumper.on()
            self._Battery.on()
            self._Clock.Active()
            self._display.showText("2: Picking up Rack")
        else:
            print("Invalid state")

    """
    Do Act for Each State
    """
    def stateEntered(self, stateno):
        if stateno == 0:        # State 0 Do Act
            self._LiftingMechanism.lowestpoint()
            self._Timer.Setatzero()
        elif stateno == 1:      # State 1 Do Act
            self._LiftingMechanism.lowestpoint()
            self._Timer.Setatzero()
        elif stateno == 2:      # State 2 Do Act
            self._Wheels.movetorack()
        else:
            print("Invalid state")
    """
    Exit Act for Each State
    """
    def stateLeft(self, stateno):
        self._display.reset()
        if stateno == 1:
            self._display.reset()
        elif stateno == 2:
            self._display.reset()
        elif stateno == 3:
            self._display.reset()
        else:
            pass

        if __name__ == "__main__":
            m = Main()
            m.run()
