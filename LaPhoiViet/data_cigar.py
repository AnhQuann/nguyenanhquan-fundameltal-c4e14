from mlab import mlab_connect
from models.cigar import Cigar

mlab_connect()

brand = {
    'Richmond': ['Cherry', 'Eu', 'King'],
    'Marlboro': ['Iceblast', 'Menthol', 'Sampoernaclove']
}

for i in brand:
    for j in brand[i]:
        cigar = Cigar(
            image = i + j + ".jpg",
            brand = i,
            cigar_type = j,
            name = "{0} {1}".format(i,j),
            # price =
        )
        cigar.save()
