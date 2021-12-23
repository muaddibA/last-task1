
def DNA_func(m, n):
    
    import Bio.Seq as bp
    from random import choice
    import numpy as np

    def DNA_GEN(length):
        
        DNA=""
        
        for count in range(length):
            DNA+=choice("CGTA")
        
        return DNA
    
    DNAS = []
    for i in range(n):
        
        myseq = bp.Seq(DNA_GEN(m))
        myseq_comp = myseq.complement()
        
        DNAS.append([myseq, myseq_comp])

    C_content_total = []
    G_content_total = []
    A_content_total = []
    T_content_total = []
    CG_content_total = []
    
    for j in DNAS:
        
        for i in range(len(j[0])):
            C_content = j[0].count('C') / (2 * len(myseq))
            G_content = j[0].count('G') / (2 * len(myseq))
            A_content = j[0].count('A') / (2 * len(myseq))
            T_content = j[0].count('T') / (2 * len(myseq))
            
            C_content += j[1].count('C') / (2 * len(myseq))
            G_content += j[1].count('G') / (2 * len(myseq))
            A_content += j[1].count('A') / (2 * len(myseq))
            T_content += j[1].count('T') / (2 * len(myseq))
            
            CG_content = G_content + C_content
            
            print(j[0][i], '-', j[1][i])
        
        C_content_total.append(C_content)
        G_content_total.append(G_content)
        A_content_total.append(A_content)
        T_content_total.append(T_content)
        CG_content_total.append(CG_content)
        
        print(f'A_content: {A_content}')
        print(f'T_content: {T_content}')
        print(f'G_content: {G_content}')
        print(f'C_content: {C_content}')
        print(f'CG_content: {CG_content}')
        print('')
        print('-----' * 10)

        print('-----' * 10)
        print('')
    
    C_content_total = np.mean(C_content_total)
    G_content_total = np.mean(G_content_total)
    T_content_total = np.mean(T_content_total)
    A_content_total = np.mean(A_content_total)
    CG_content_total = np.mean(CG_content_total)
    
    print(f'Среднее содержание Аденина: {A_content_total}', f'Среднее содержание Тимина: {T_content_total}', f'Среднее содержание Гуанина: {G_content_total}', f'Среднее содержание Цитозина: {C_content_total}', f'Cредний показатель GC content: {CG_content_total}', sep = '\n')
    
    return DNAS, A_content_total, T_content_total, G_content_total, C_content_total, CG_content_total