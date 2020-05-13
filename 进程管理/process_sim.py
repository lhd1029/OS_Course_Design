import time
PROCESS_MAXNUM = 100


class PCB:
    file_list = []  # 打开文件列表
    io = []  # IO使用情况(列表)
    # cpureg = CPUREG()

    def __init__(self, pid_, state_, address_code_, address_process_, code_space_, priority_):
        self.pid = pid_  # pid
        self.state = state_  # ready, running, waiting, terminated
        self.address_code = address_code_  # 代码段首地址
        self.address_process = address_process_  # 进程活动空间首地址
        self.code_space = code_space_  # 代码段长度
        self.priority = priority_  # 进程优先级


def if_create_PCB():
    if PCB_queue.size() == PROCESS_MAXNUM:
        return False
    else:
        return True


def move_from_running_to_waiting(pid, waiting_queue, ready_queue, PCB_queue):
    waiting_queue.remove(pid)
    ready_queue.append(pid)
    PCB_queue[pid].state = "waiting"


def move_from_waiting_to_ready(pid, waiting_queue, ready_queue, PCB_queue):
    waiting_queue.remove(pid)
    ready_queue.append(pid)
    PCB_queue[pid].state = "ready"


def move_from_running_to_ready(pid, ready_queue, PCB_queue):
    ready_queue.append(pid)
    PCB_queue[pid].state = "ready"


def move_from_ready_to_running(pid, ready_queue, PCB_queue):
    ready_queue.remove(pid)
    PCB_queue[pid].state = "running"


def start_process(q):
    while (1):
        time.sleep(1)
        print("A")
