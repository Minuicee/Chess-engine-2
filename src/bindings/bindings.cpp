#include "pybind11/pybind11.h"
#include "../cpp/engine.h"

namespace py = pybind11;

PYBIND11_MODULE(engine, m) {
    m.def("hello", []() { return "Test"; });
    // Hier alle Funktionen/Klassen einbinden, die du nach Python bringen willst
}
