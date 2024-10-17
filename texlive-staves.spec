Name:		texlive-staves
Version:	15878
Release:	2
Summary:	Typeset Icelandic staves and runic letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/staves
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains all the necessary tools to typeset the
"magical" Icelandic staves plus the runic letters used in
Iceland. Included are a font in Adobe Type 1 format and LaTeX
support.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/staves/icelandic.map
%{_texmfdistdir}/fonts/tfm/public/staves/icelandic.tfm
%{_texmfdistdir}/fonts/type1/public/staves/icelandic.pfb
%{_texmfdistdir}/tex/latex/staves/staves.sty
%doc %{_texmfdistdir}/doc/fonts/staves/README
%doc %{_texmfdistdir}/doc/fonts/staves/staves.pdf
%doc %{_texmfdistdir}/doc/fonts/staves/symbols.pdf
#- source
%doc %{_texmfdistdir}/source/latex/staves/staves.dtx
%doc %{_texmfdistdir}/source/latex/staves/staves.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
