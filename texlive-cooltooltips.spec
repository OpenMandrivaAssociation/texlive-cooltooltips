Name:		texlive-cooltooltips
Version:	60201
Release:	2
Summary:	Associate a pop-up window and tooltip with PDF hyperlinks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cooltooltips
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooltooltips.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooltooltips.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cooltooltips.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/cooltooltips
%doc %{_texmfdistdir}/doc/latex/cooltooltips
#- source
%doc %{_texmfdistdir}/source/latex/cooltooltips

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
