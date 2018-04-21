Go Game Guru Problems - PDF Generation
=======================================

After I stumbled on [Go Game Guru Problems Github Page](https://github.com/gogameguru/go-problems) and went over the PDF
files it generated I realised that I personally like a different type of approach to problem solving.

I like a single PDF with all the problems and only opening up solutions when I'm stuck or I want to make sure I was correct.

Get the files
=====================

* [Easy Problems](https://github.com/toomasr/ggg-problems-latex/raw/master/releases/easy-problems.pdf)
* [Intermediate Problems](https://github.com/toomasr/ggg-problems-latex/raw/master/releases/intermediate-problems.pdf)
* [Hard Problems](https://github.com/toomasr/ggg-problems-latex/raw/master/releases/hard-problems.pdf)

What about the solutions? You can grab the solutions from [Go Game Guru Github Page](https://github.com/gogameguru/go-problems). Here is
the direct link if it is still working - [Solutions in PDF](https://gogameguru.com/i/go-problems/download/weekly-go-problems-pdf.zip).

Technical details about the project
=====================

The project uses the bundled PNG files to generate a gigantic [LaTeX](https://www.latex-project.org/) file and then process that with
the LaTeX system. I came up with a simple Tex file that looks good enough for my needs. You can find the parts of the file under 
[src/templates](https://github.com/toomasr/ggg-problems-latex/tree/master/src/templates).

Then I use `src/generate.py` to generate these gigantic tex files and then `pdflatex` produces the final PDF files. The TeX files overall looks something like this.

```latex
\documentclass[10pt]{book}

\usepackage{graphicx}
\usepackage[font={small}]{caption}
\captionsetup[figure]{labelsep=space}

\renewcommand{\figurename}{Problem}

\usepackage
[
    a4paper,
    left=0.1cm,
    right=0.1cm
]
{geometry}

\pagestyle{plain}
\begin{document}

\begin{figure}[t]
        \begin{minipage}{0.5\textwidth}
            \centering
            \includegraphics[height=2.0in]{problems/easy/ggg-easy-001.png}
            \caption{}
        \end{minipage}%
        \begin{minipage}{0.5\textwidth}
            \centering
            \includegraphics[height=2.0in]{problems/easy/ggg-easy-002.png}
            \caption{}
        \end{minipage}
\end{figure}

\begin{figure}[t]
        \begin{minipage}{0.5\textwidth}
            \centering
            \includegraphics[height=2.0in]{problems/easy/ggg-easy-003.png}
            \caption{}
        \end{minipage}%
        \begin{minipage}{0.5\textwidth}
            \centering
            \includegraphics[height=2.0in]{problems/easy/ggg-easy-004.png}
            \caption{}
        \end{minipage}
\end{figure}

\begin{figure}[t]
        \begin{minipage}{0.5\textwidth}
            \centering
            \includegraphics[height=2.0in]{problems/easy/ggg-easy-005.png}
            \caption{}
        \end{minipage}%
        \begin{minipage}{0.5\textwidth}
            \centering
            \includegraphics[height=2.0in]{problems/easy/ggg-easy-006.png}
            \caption{}
        \end{minipage}
\end{figure}

\clearpage

% more and more such blocks

\end{document}
```

I hope this LaTeX file might be useful some other places where you need to have two columns of problem figures.
