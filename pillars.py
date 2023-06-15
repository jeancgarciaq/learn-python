# **********************
# POSTES EN LA CARRETERA
# **********************


def run(num_pillars: int, gap_pillars: float, pillar_width: float) -> float:
    # TU C�DIGO AQU�
    
    anchomenos = pillar_width * 2
    distanciaposte = gap_pillars * 100
    anchurapostes = pillar_width * num_pillars - anchomenos
    calculo = distanciaposte * (num_pillars - 1) + anchurapostes
    inter_distance = calculo

    return inter_distance



if __name__ == '__main__':
    run(10, 5, 30)