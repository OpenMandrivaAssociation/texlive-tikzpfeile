Name:		texlive-tikzpfeile
Version:	25777
Release:	2
Summary:	Draw arrows using PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikzpfeile
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpfeile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpfeile.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzpfeile.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In a document with a lot of diagrams created with PGF/TikZ,
there is a possibility of the reader being distracted by
different sorts of arrowheads in the diagrams and in the text
(as, e.g., in \rightarrow). The package defines macros to
create all arrows using PGF/TikZ, so as to avoid the problem.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikzpfeile/tikzpfeile.sty
%doc %{_texmfdistdir}/doc/latex/tikzpfeile/README
%doc %{_texmfdistdir}/doc/latex/tikzpfeile/tikzpfeile.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tikzpfeile/tikzpfeile.dtx
%doc %{_texmfdistdir}/source/latex/tikzpfeile/tikzpfeile.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
