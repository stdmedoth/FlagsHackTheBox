if ! sudo --version | head -1 | grep -qE '(1\.8.*|1\.9\.[0-9]1?(p[1-3])?|1\.9\.12p1)$'
then
    echo "> Currently installed sudo version is not vulnerable"
    exit 1
fi
