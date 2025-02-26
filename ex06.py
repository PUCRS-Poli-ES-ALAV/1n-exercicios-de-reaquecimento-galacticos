def seq_ack(n1,n2):
    if n1 == 0:
        return n2 + 1 
    if n1 != 0 and n2 == 0:
        return seq_ack(n1-1,1)
    if n1 !=0 and n2 != 0:
        return seq_ack(n1 - 1, seq_ack(n1,n2-1))
    
seq_ack(2,2)