def calculate_fine(days_late):
    if days_late <= 0:
        return 0
    if days_late <= 7:
        return days_late * 2
    if days_late <= 30:
        return 14 + (days_late - 7) * 3
    return 83 + (days_late - 30) * 5

