def get_list(item, index):
    ir = item[index]['itemresponses']
    irList = [int(i) for i in ir.split(',')]
    return irList