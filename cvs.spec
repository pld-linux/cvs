Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(fr):	CVS : Concurrent Versioning System
Summary(pl):	Concurrent Versioning System
Summary(tr):	Sürüm denetim sistemi
Name:		cvs
Version:	1.10.7
Release:     	2
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarzadzanie wersjami
Source0:	http://download.cyclic.com/pub/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		cvs-tmprace.patch
Patch1:		cvs-info.patch
Patch2:		cvs-1.10.6-v6-19990629-PLD.patch
URL:		http://www.cyclic.com/
Prereq:		/usr/sbin/fix-info-dir
Buildroot:	/tmp/%{name}-%{version}-root

%description
CVS is a front end to the rcs(1) revision control system which extends the
notion of revision control from a collection of files in a single directory
to a hierarchical collection of directories consisting of revision
controlled files. These directories and files can be combined together to
form a software release. CVS provides the functions necessary to manage
these software releases and to control the concurrent editing of source
files among multiple software developers.

%description -l de
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den Begriff
der Revisionskontrolle von einer Sammlung von Dateien in einem einzelnen
Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend aus
revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien lassen sich
zu einer Software-Release kombinieren. CVS bietet die Funktionen, die zur
Verwaltung von Software-Releases und zur Überwachung der gleichzeitigen
Bearbeitung von Quelldateien durch mehrere Software- Entwickler notwendig
sind.

%description -l fr
CVS est un frontal pour le système de contrôle de révision rcs(1) qui étend
la notion de contrôle de révision d'un ensemble de fichiers placés dans un
seul répertoire à un ensemble hiérarchisé de répertoires contenant des
fichiers contrôlés. Ces répertoires et fichiers peuvent être combinés pour
former une version de logiciel. CVS offre les fonctions nécessaires pour
gérer ces versions et pour contrôler la modification simultanée des fichiers
sources entre les différents déeloppeurs.

%description -l pl
CVS jest nak³adk± na rcs (Revision Control System, czyli w wolnym
t³umaczeniu system kontroli wersji zasobów), który rozszerza mo¿liwo¶ci
rcs'a z narzêdzia do kontroli zbioru plików w pojedynczym katalogu o
mo¿liwo¶æ kontroli zbioru hierarhicznie u³o¿onych katalogów z plikami. Z
pomoc± CVS w ³atwy sposób mo¿na zarz±dzaæ kodem ¼ród³owym opracowywanym przez
nawet bardzo du¿e zespó³y programistów umo¿liwiaj±c ¶ledzenie i kontrolê
wszystkich zmian w trakcie pracy nad projektami i wypuszczaniem pe³nych
wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya topluluðunun
sürüm denetimini, denetimi yapýlmýþ dizinlerin hiyerarþik topluluðuna
geniþleten rcs(1) sürüm denetim sisteminin ön yüzüdür. Bu dizin ve dosyalar,
bir yazýlým yayýný oluþturma amacýyla biraraya getirilebilir. CVS, bu
yazýlým yayýnlarýnýn yönetilmesini ve kaynak dosyalarý bakýmýnýn birden çok
yazýlým geliþtiricisi tarafýndan eþzamanlý olarak yapýlmasýný kontrol etmek
için gereken iþlevleri saðlar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-ipv6 \
	--enable-server \
	--enable-client
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	mandir=$RPM_BUILD_ROOT%{_mandir}
make install-info \
	prefix=$RPM_BUILD_ROOT%{_prefix} \
	infodir=$RPM_BUILD_ROOT%{_infodir}

strip $RPM_BUILD_ROOT%{_bindir}/cvs

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/cvs*,%{_mandir}/man{1,5,8}/*} \
	doc/*.ps BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,FAQ,MINOR-BUGS,NEWS,PROJECTS,TODO,README,ChangeLog}.gz
%doc doc/*.ps.gz contrib/*

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[158]/*
%{_infodir}/cvs*
