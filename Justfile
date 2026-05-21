build package:
    #!/usr/bin/env bash
    set -euo pipefail
    mkdir -p rpmbuild/SPECS
    cp packages/{{ package }}.spec rpmbuild/SPECS/{{ package }}.spec
    podman run --rm --pull newer -i -e PACKAGE={{ package }} -v ./rpmbuild:/root/rpmbuild:Z,rw quay.io/fedora/fedora:latest << 'EOF'
    set -euo pipefail
    dnf install -y rpmdevtools
    SPECFILE="/root/rpmbuild/SPECS/${PACKAGE}.spec"
    spectool -g -R "$SPECFILE"
    dnf builddep -y "$SPECFILE"
    rpmbuild -ba "$SPECFILE"
    EOF
