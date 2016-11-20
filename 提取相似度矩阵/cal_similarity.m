v = var(DLU(:));
for i=1:1343
    for j = 1:1343
        SLU(i, j) = 1/exp((DLU(i, j)^2)/v);
    end
end