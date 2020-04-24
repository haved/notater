(TeX-add-style-hook
 "Krets"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("article" "12pt" "a4paper" "norsk")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "norsk") ("circuitikz" "siunitx" "american" "europeanresistors" "RPvoltages") ("parskip" "skip=5mm")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art12"
    "inputenc"
    "babel"
    "hyperref"
    "amsmath"
    "amssymb"
    "amstext"
    "array"
    "siunitx"
    "subcaption"
    "float"
    "booktabs"
    "circuitikz"
    "graphicx"
    "parskip"
    "caption")
   (TeX-add-symbols
    '("ubercol" 1)
    '("kom" 1)
    '("var" 1)
    '("resi" 1)
    "varkern"
    "xor"
    "xnor")
   (LaTeX-add-labels
    "fig:capacitor_Q"
    "fig:capacitor_VDD"
    "sec:spoler"
    "sec:dioder"
    "fig:nMOS"
    "sec:cmos"
    "fig:CMOS_NAND"
    "sec:bool_alg"
    "sec:logiske_porter"
    "fig:porter"
    "sec:forsinkelser"
    "fig:delay"
    "fig:kritisk_sti"
    "sec:kritisk_sti"
    "sec:bool_func"
    "table:minterm"
    "sec:datablader"
    "sec:logic_circuits"
    "sec:ripple_carry_fulladder"
    "sec:tekonologimapping"
    "fig:SR-latch"
    "tab:SR-latch"
    "tab:SR_latch_eksit"
    "fig:D-latch"
    "tab:D-latch"
    "tab:D-latch-eksit"
    "fig:master_slave"
    "fig:trigger_shift")
   (LaTeX-add-array-newcolumntypes
    "C"))
 :latex)

