%global tl_name staves
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typeset Icelandic staves and runic letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/staves
License:	lppl1.3b
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/staves.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains all the necessary tools to typeset the "magical"
Icelandic staves plus the runic letters used in Iceland. Included are a
font in Adobe Type 1 format and LaTeX support.

