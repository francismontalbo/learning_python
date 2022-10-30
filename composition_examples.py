#COMPOSITION EXAMPLES

#THESE ARE THE COMPONENT CLASSES!
class RAM:
    def __init__(self, ram_size):
        self.ram_size = ram_size
        
    @staticmethod
    def ram_storing():
        print('RAM storing!....')

       
class CPU:
    def __init__(self, cpu_speed):
        self.cpu_speed = cpu_speed
    
    @staticmethod
    def cpu_processing():
        print('CPU processing!....')
     
   
class GPU:
    def __init__(self, gpu_memory):
        self.gpu_memory = gpu_memory
    
    @staticmethod
    def gpu_running():
        print('GPU is initializing....')


#This is the COMPOSITE CLASS
class Computer:
    def __init__(self, ram, cpu, gpu):
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
    
    def boot(self):
        print('PC booting....!'.upper())
    
    @property
    def post_info(self):
        print(f'The GPU memory is currently: {float(self.gpu.gpu_memory)}GB')
        print(f'The CPU speed is currently: {float(self.cpu.cpu_speed)}GHz')
        print(f'The RAM memory is currently: {float(self.ram.ram_size)}GB')
        

computer = Computer(RAM(8), CPU(25), GPU(12))

def run_computer(pc):
    switch = int(input('Do you want to turn on the computer?\n1-Yes\n2-No\n'))
    if switch == 1:
        print(f'The user selected option {switch}.')
        print('*'*50)
        pc = computer
        computer.boot()
        print('*'*50)
        computer.ram.ram_storing()
        computer.cpu.cpu_processing()
        computer.gpu.gpu_running()
        print('.\n'*5)
        print('PC initialized successfully!\n' + '...' * 10)
        computer.post_info
    elif switch == 2:
        print('The computer stayed OFF')


run_computer(computer)








