Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(fr):	Un système pour maintenir à jour des fichiers
Summary(pl):	Concurrent Versioning System
Summary(tr):	Sürüm denetim sistemi
Name:		cvs
Version:	1.10.8
Release:	1
License:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz±dzanie Wersjami
Source0:	http://download.cyclic.com/pub/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:		cvs-tmprace.patch
Patch1:		cvs-info.patch
Patch2:		http://www.misiek.eu.org/ipv6/cvs-ipv6-220200.patch.gz
URL:		http://www.cyclic.com/
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS means Concurrent Version System; it is a version control system which
can record the history of your files (usually, but not always, source
code). CVS only stores the differences between versions, instead of every
version of every file you've ever created. CVS also keeps a log of who,
when and why changes occurred, among other aspects.  CVS is very helpful
for managing releases and controlling the concurrent editing of source
files among multiple authors. Instead of providing version control for a
collection of files in a single directory, CVS provides version control for
a hierarchical collection of directories consisting of revision controlled
files.  These directories and files can then be combined together to form a
software release.

%description -l de
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend aus
revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien lassen
sich zu einer Software-Release kombinieren. CVS bietet die Funktionen, die
zur Verwaltung von Software-Releases und zur Überwachung der gleichzeitigen
Bearbeitung von Quelldateien durch mehrere Software- Entwickler notwendig
sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un système de comparaison
de versions de fichiers, qui peut garder une trace des changements apportés
à des fichiers (le plus souvent, les fichiers des sources d'un programme).
CVS conserve seulement les différences, et non l'intégralité d'un fichier
récent et d'un fichier plus ancien. A chaque modification d'un fichier, CVS
garde (entre autres) le nom de la personne ayant fait la modification, la
raison justifiant cette modification, et la date à laquelle celle-ci a eu
lieu.  CVS est très utile pour gérer la mise en commun des modifications
apportées par plusieurs personnes travaillant en parallèle sur les mêmes
fichiers. Au lieu de garder plusieurs versions des fichiers dans un seul
répertoire, CVS crée une série de répertoires, chacun contenant une
nouvelle version des fichiers. Ces répertoires et ces fichiers peuvent
ensuite être regroupés pour former la version la plus à jour du logiciel.
Installez ce package si vous avez besoin d'utiliser un système de contrôle
de version.

%description -l pl
CVS jest nak³adk± na rcs (Revision Control System, czyli w wolnym
t³umaczeniu system kontroli wersji zasobów), który rozszerza mo¿liwo¶ci
rcs'a z narzêdzia do kontroli zbioru plików w pojedynczym katalogu o
mo¿liwo¶æ kontroli zbioru hierarhicznie u³o¿onych katalogów z plikami. Z
pomoc± CVS w ³atwy sposób mo¿na zarz±dzaæ kodem ¼ród³owym opracowywanym
przez nawet bardzo du¿e zespó³y programistów umo¿liwiaj±c ¶ledzenie i
kontrolê wszystkich zmian w trakcie pracy nad projektami i wypuszczaniem
pe³nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya topluluðunun
sürüm denetimini, denetimi yapýlmýþ dizinlerin hiyerarþik topluluðuna
geniþleten rcs(1) sürüm denetim sisteminin ön yüzüdür. Bu dizin ve
dosyalar, bir yazýlým yayýný oluþturma amacýyla biraraya getirilebilir.
CVS, bu yazýlým yayýnlarýnýn yönetilmesini ve kaynak dosyalarý bakýmýnýn
birden çok yazýlým geliþtiricisi tarafýndan eþzamanlý olarak yapýlmasýný
kontrol etmek için gereken iþlevleri saðlar.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
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

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/cvs*,%{_mandir}/man{1,5,8}/*} \
	doc/*.ps BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog

%post
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,FAQ,MINOR-BUGS,NEWS,PROJECTS,TODO,README,ChangeLog}.gz
%doc doc/*.ps.gz contrib/*

%attr(755,root,root) %{_bindir}/*

%{_mandir}/man[158]/*
%{_infodir}/cvs*
