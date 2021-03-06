from typing import List

def getEvents() -> Events: ...
def getMousePosition() -> Vector2: ...
def setMousePosition(int x, int y) -> None: ...

def getWindowSize() -> engine.Vector2: ...
def quitGame() -> None: ...
def getCurrentScene() -> Scene: ...
def setScene(sceneName : str) -> None: ...

class Events:
	def pressed(self, event : str) -> bool: ...
	def active(self, event : str) -> bool: ...
	def released(self, event : str) -> bool: ...
	

class Entity:
	name : str
	def kill(): ...
	def hasTag(tag : str) -> bool: ...
	def add(component : Component) -> None: ...
	def get(component : str) -> Component: ...
	def getAll(component : str) -> list(Component): ...
	def getScene() -> Scene: ...
	def getParent() -> Entity: ...
	def getChildren() -> list(Entity): ...
	def getTransform() -> TransformComponent: ...
	def getID() -> int: ...


class RayCastOut:
	hit : bool
	position : Vector3
	normal : Vector3
	entity : Entity


class Scene:
	def newEntity() -> Entity: ...
	def add(entity : Entity) -> Entity: ...
	def addFromTemplate(templateName : str, overrideTransform=True) -> Entity: ...
	def remove(entity : Entity) -> None: ...
	def rayCast(origin : Vector3, target : Vector3) -> RayCastOut: ...
	def getSun() -> Sun: ...


class Sun:
	hour : float # 0.0 to 24.0
	angle : float #0.0 to 360.0
	color : Vector3
	intensity : float


class Timer:
	def get() -> float: ...
	def set(value : float) -> None: ...
	def reset() -> None: ...


###############################################################################


class Component:
	entity : Entity

	def start(scene : Scene)-> None:
		"""Override thid Method and it will be called by the entity when added to the scene."""
		pass

	def update()-> None:
		"""Override thid Method and it will be called every frame."""
		pass
	
	def end(scene : Scene)-> None:
		"""Override thid Method and it will be called by the entity when removed from the scene."""
		pass


class TransformComponent(Component):
	position : Vector3
	scale : Vector3

	def getEuler() -> Vector3: ...
	def setEuler(euler : Vector3): ...
	def setEuler(x : float, y : float, z : float): ...

	def getQuaternion() -> Quaternion: ...
	def setQuaternion(quaternion : Quaternion): ...
	def setQuaternion(x : float, y : float, z : float, w: float): ...

	def getMatrix() -> Matrix4: ...
	def setMatrix(mat : Matrix4): ...

	def rotateVector(vec : Vector3) -> Vector3: ...
	def transformVector(vec : Vector3) -> Vector3: ...

	def rotate(x : float, y : float, z : float) -> None: ...
	def move(x : float, y : float, z : float, local = True): ...

	def rotateOnAxis(angle : float, axis : Vector3) -> None: ...
	def rotateOnPitch(angle : float) -> None: ...
	def rotateOnYaw(angle : float) -> None: ...
	def rotateOnRoll(angle : float) -> None: ...
	def applyLocalMovement(x : float, y : float, z : float) -> None: ...
	def getPitch() -> float: ...
	def getYaw() -> float: ...
	def getRoll() -> float: ...
	def getForwardVector() -> Vector3: ...
	def getRightVector() -> Vector3: ...
	def getUpVector() -> Vector3: ...
	def lookAt(direction : Vector3, up = Vector3(0, 1, 0)) -> None: ...


class MeshComponent(Component):
	def setAnimation(animation : string) -> None: ...


class LightComponent(Component):
	color : Vector3
	radius : float
	intensity : float


class UIElementComponent(Component):
	text : str
	position : UIVector
	scale : UIVector
	text : str

	def isHovered() -> bool: ...


class RigidBodyComponent(Component):
	alwaysActive : bool
	linearVelocity : engine.Vector3
	angularVelocity : engine.Vector3
	angularFactor : engine.Vector3

	def getCollisions() -> list(Entity): ...
	def collidedWith(tag : string) -> bool: ...
	def applyTorque(x : float, y : float, z : float) -> None: ...
	def applyForce(x : float, y : float, z : float, location : Vector3) -> None: ...
	def isDynamic() -> bool: ...
	def setMass(value : float) -> None: ...


###############################################################################
# Math


def normalized(vec : Vector3) -> Vector3: ...

def length(vec : Vector3) -> float: ...


class Vector2:
	x : float
	y : float

	# Equivalents:
	s : float
	t : float

	x : float
	y : float


class Vector3:
	x : float
	y : float
	z : float

	# Equivalents:
	r : float
	g : float
	b : float


class Vector4:
	x : float
	y : float
	z : float
	w : float

	# Equivalents:
	r : float
	g : float
	b : float
	a : float


class Quaternion:
	x : float
	y : float
	z : float
	w : float


class UIVector:
	anchoringX : int # -1, 0, 1
	anchoringY : int # -1, 0, 1

	def isRelativeX() -> bool: ...
	def isRelativeY() -> bool: ...
	def getX(parentScale = 1.0) -> float: ...
	def getY(parentScale = 1.0) -> float: ...
	def setPixelX(value : int) -> None: ...
	def setPixelY(value : int) -> None: ...
	def setPixel(x : int, y : int) -> None: ...
	def setRelativeX(value : float) -> None: ...
	def setRelativeY(value : float) -> None: ...
	def setRelative(x : float, y : float) -> None: ...