from juju.system import System

def test_system_instantiation(): 
	s = System()
	assert isinstance(s,System)

