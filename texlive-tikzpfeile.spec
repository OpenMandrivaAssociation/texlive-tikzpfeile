%global tl_name tikzpfeile
%global tl_revision 25777

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Draw arrows using PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpfeile
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpfeile.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpfeile.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpfeile.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In a document with a lot of diagrams created with PGF/TikZ, there is a
possibility of the reader being distracted by different sorts of
arrowheads in the diagrams and in the text (as, e.g., in \rightarrow).
The package defines macros to create all arrows using PGF/TikZ, so as to
avoid the problem.

