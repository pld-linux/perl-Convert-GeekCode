#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	GeekCode
Summary:	Convert::GeekCode - Convert and generate geek code sequences
Summary(pl):	Modu³ Convert::GeekCode - generuj±cy i konwertuj±cy sekwencje ,,geek code''
Name:		perl-Convert-GeekCode
Version:	0.5
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%{!?_without_tests:BuildRequires:	perl-YAML}
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::GeekCode converts and generates Geek Code sequences (cf.
http://geekcode.com/). It supports different langugage codes and
user-customizable codesets.

%description -l pl
Modu³ Convert::GeekCode konwertuje i generuje sekwencje Geek Code
(http://geekcode.com/). Obs³uguje kody dla ró¿nych jêzyków i zestawy
kodów definiowane przez u¿ytkownika.

%package -n geekcode-tools
Summary:	geekdec - Geek Code decoder, geekgen - Geek Code generator
Summary(pl):	geekdec - dekoder i geekgen - generator Geek Code
Group:		Applications
Requires:	%{name}

%description -n geekcode-tools
geekdec parses Geek Code sequences read from the standard input, and
prints out explanations.

geekgen generates Geek Code sequences interactively, according to
user's input. User could mix numerical selections with usual symbols
like (), >, ! and @.

%description -n geekcode-tools -l pl
geekdec analizuje sekwencje Geek Code czytane ze standardowego wyj¶cia
i wypisuje ich znaczenie.

geekgen generuje sekwencje Geek Code interaktywnie, zgodnie z danymi
wprowadzanymi przez u¿ytkownika. U¿ytkownik mo¿e mieszaæ numery opcji
ze zwykle u¿ywanymi symbolami takimi jak (), >, ! i @.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*

%files -n geekcode-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
