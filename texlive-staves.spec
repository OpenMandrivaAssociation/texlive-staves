# revision 15878
# category Package
# catalog-ctan /language/staves
# catalog-date 2008-08-23 15:48:35 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-staves
Version:	20080823
Release:	1
Summary:	Typeset Icelandic staves and runic letters. 
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/staves
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package contains all the necessary tools to typeset the
"magical" Icelandic staves plus the runic letters used in
Iceland. Included are a font in Adobe Type 1 format and LaTeX
support.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
