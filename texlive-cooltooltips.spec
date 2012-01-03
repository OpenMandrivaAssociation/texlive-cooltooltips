# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/cooltooltips
# catalog-date 2007-03-05 15:26:58 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-cooltooltips
Version:	1.0
Release:	2
Summary:	Associate a pop-up window and tooltip with PDF hyperlinks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cooltooltips
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooltooltips.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooltooltips.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooltooltips.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cooltooltips package enables a document to contain
hyperlinks that pop up a brief tooltip when the mouse moves
over them and also open a small window containing additional
text. cooltooltips provides the mechanism used by the Visual
LaTeX FAQ to indicate the question that each hyperlink answers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cooltooltips/cooltooltips.sty
%doc %{_texmfdistdir}/doc/latex/cooltooltips/README
%doc %{_texmfdistdir}/doc/latex/cooltooltips/cooltooltips.pdf
#- source
%doc %{_texmfdistdir}/source/latex/cooltooltips/cooltooltips.dtx
%doc %{_texmfdistdir}/source/latex/cooltooltips/cooltooltips.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
