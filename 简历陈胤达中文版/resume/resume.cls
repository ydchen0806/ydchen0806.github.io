% ========================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{resume}
\LoadClass[10pt]{article}
% ========================================================================
\setlength{\parindent}{0pt}
% ========================================================================
\RequirePackage{xltxtra}
\RequirePackage{xifthen}
\RequirePackage{progressbar}
% ========================================================================
\RequirePackage{url}
\urlstyle{tt}
% ========================================================================
\RequirePackage{fontawesome}
\RequirePackage{fontspec}
% ========================================================================
\setmainfont[
  Path = fonts/Main/ ,
  Extension = .otf ,
  UprightFont = *-regular ,
  BoldFont = *-bold ,
  ItalicFont = *-italic ,
  BoldItalicFont = *-bolditalic ,
  SmallCapsFont = Fontin-SmallCaps
]{texgyretermes}
% ========================================================================
\RequirePackage[a4paper, left=15mm, right=15mm, top=5mm, bottom=5mm, nohead]{geometry}
% ========================================================================
% ========================================================================
\RequirePackage{titlesec}
\RequirePackage{enumitem}
\setlist{noitemsep}
\setlist[itemize]{topsep=0.1em, leftmargin=1.5pc}
\setlist[enumerate]{topsep=0.1em, leftmargin=1.5pc}
\RequirePackage[super]{nth}
% ========================================================================
% ========================================================================
\titleformat{\section}
  {\large\scshape\raggedright}
  {}{0em}
  {}
  [\vspace{-.666em}\rule{18cm}{1.5pt}\vspace{-.666em}]
\titlespacing*{\section}{0cm}{*.5}{*1.25}
\titleformat{\subsection}
  {\kaishu\large\raggedright}
  {}{0em}
  {}
\titlespacing*{\subsection}{0cm}{*.5}{*.5}
% ========================================================================
\newcommand{\datedsection}[2]{\section[#1]{#1 \hfill #2}}
\newcommand{\datedsubsection}[2]{\subsection[#1]{#1 \hfill #2}}
\newcommand{\datedline}[2]{{\par #1 \hfill #2 \par}}
\newcommand{\name}[1]{\centerline{\Huge\scshape{#1}}\vspace{1em}}
\newcommand{\nameTest}[1]{{\large\scshape{#1}}}
% ========================================================================
\newcommand{\email}[1]{\faEnvelope{\textbf{#1}}}
% ========================================================================
\newcommand{\phone}[1]{\faPhone{\textbf{#1}}}
% ========================================================================
\newcommand{\Wechat}[1]{\faWechat{\textbf{#1}}}
% ========================================================================
\newcommand{\linkedin}[2][]{\faLinkedin\ 
    \ifthenelse{\isempty{#1}}
    {\href{#2}{#2}}
    {\href{#2}{#1}}
    }%%
% ========================================================================
\newcommand{\github}[2][]{\faGithub\ 
    \ifthenelse{\isempty{#1}}
    {\href{#2}{#2}}
    {\href{#2}{#1}}
    }%%
% ========================================================================
\newcommand{\homepage}[2][]{\faLink\
    \ifthenelse{\isempty{#1}}
    {\href{#2}{#2}}{\href{#2}{#1}}
    }%%
% ========================================================================
\newcommand{\pbar}[3][10em]{{#2}\ 
    \progressbar[heightr=1, width=#1, borderwidth=0pt, roundnessr=0.45, filledcolor=green!40, subdivisions=1]{#3}
    }%%
% ========================================================================
\newcommand{\basicInfo}[1]{\centerline{\ttfamily\large{#1}}\vspace{1.25ex}}
\newcommand{\role}[2]{
    \vspace{-.2em}
    {\par \textbf{\kaishu #1} ~ \textit{#2}}
    \vspace{-.2em}
    }%%