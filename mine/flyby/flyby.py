import rebound
from numpy import pi as PI

n_p = 100


def hearbeat(sim_pointer):
    pass

sim = rebound.Simulation()

# // Start the REBOUND visualization server. This
# // allows you to visualize the simulation by pointing
# // your web browser to http://localhost:1234
# // The particles are tiny in this example. To see them
# // on the screen press `s` to change their plotting style.

sim.start_server(port=1234)

# Simulation Setup
# r->integrator    = REB_INTEGRATOR_MERCURIUS;
sim.heartbeat = hearbeat
sim.dt = 4./365.25*2.*PI # 4 days
sim.integrator = 'whfast'
sim.N_active = 2

sim.add(m=1.)                # Sun
sim.add(m=1, a=1., e=0.1) # Stellar flyby

# move origin to COM
sim.move_to_com()

# test particles
for i in range(n_p):
    pass




# integrate
sim.integrate()

# clean up
sim = None