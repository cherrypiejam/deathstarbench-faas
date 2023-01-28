{ pkgs ? import <nixpkgs> {} }:

with pkgs;

mkShell {
    buildInputs = [
        kompose
        kubectl
        kubernetes
        kubernetes-helm
        minikube
        faas-cli
        arkade
        (python39.withPackages (p: with p; [
            pytest names requests
        ]))
    ];
}
