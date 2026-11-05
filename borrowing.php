<?php
function canBorrow(int $activeLoans, bool $hasOverdue): bool {
    if ($hasOverdue) return false;
    if ($activeLoans >= 3) return false;
    return true;
}
