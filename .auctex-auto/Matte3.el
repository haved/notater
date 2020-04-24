(TeX-add-style-hook
 "Matte3"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt" "a4paper" "norsk")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "norsk") ("parskip" "skip=5mm")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "inputenc"
    "babel"
    "amssymb"
    "amsmath"
    "multicol"
    "appendix"
    "siunitx"
    "parskip")
   (TeX-add-symbols
    '("inner" 1)
    '("mat" 2)
    '("overskrift" 1)
    '("imat" 1)
    "R"
    "C"
    "B"
    "breather"
    "nullvec"
    "nullmat"
    "Sp"
    "Col"
    "Row"
    "Null"
    "image"
    "rank"
    "Ima"
    "Rea"
    "vv"
    "vw"
    "vu"
    "vx"
    "vy"
    "vq")
   (LaTeX-add-labels
    "sec:rank-nullity"
    "sec:ikke-inverterbare_matriser"
    "sec:indreprodukt"
    "sec:ortogonalt_komplement"
    "eq:ai"
    "sec:symmetriske_matriser"
    "sec:minste_kvadraters_metode"
    "eq:PSUM"))
 :latex)

