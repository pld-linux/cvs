Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(fr):	Un syst�me pour maintenir � jour des fichiers
Summary(pl):	Concurrent Versioning System
Summary(tr):	S�r�m denetim sistemi
Name:		cvs
Version:	1.10.8
Release:	1
License:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarz�dzanie Wersjami
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
CVS ist ein Frontend f�r das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend aus
revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien lassen
sich zu einer Software-Release kombinieren. CVS bietet die Funktionen, die
zur Verwaltung von Software-Releases und zur �berwachung der gleichzeitigen
Bearbeitung von Quelldateien durch mehrere Software- Entwickler notwendig
sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un syst�me de comparaison
de versions de fichiers, qui peut garder une trace des changements apport�s
� des fichiers (le plus souvent, les fichiers des sources d'un programme).
CVS conserve seulement les diff�rences, et non l'int�gralit� d'un fichier
r�cent et d'un fichier plus ancien. A chaque modification d'un fichier, CVS
garde (entre autres) le nom de la personne ayant fait la modification, la
raison justifiant cette modification, et la date � laquelle celle-ci a eu
lieu.  CVS est tr�s utile pour g�rer la mise en commun des modifications
apport�es par plusieurs personnes travaillant en parall�le sur les m�mes
fichiers. Au lieu de garder plusieurs versions des fichiers dans un seul
r�pertoire, CVS cr�e une s�rie de r�pertoires, chacun contenant une
nouvelle version des fichiers. Ces r�pertoires et ces fichiers peuvent
ensuite �tre regroup�s pour former la version la plus � jour du logiciel.
Installez ce package si vous avez besoin d'utiliser un syst�me de contr�le
de version.

%description -l pl
CVS jest nak�adk� na rcs (Revision Control System, czyli w wolnym
t�umaczeniu system kontroli wersji zasob�w), kt�ry rozszerza mo�liwo�ci
rcs'a z narz�dzia do kontroli zbioru plik�w w pojedynczym katalogu o
mo�liwo�� kontroli zbioru hierarhicznie u�o�onych katalog�w z plikami. Z
pomoc� CVS w �atwy spos�b mo�na zarz�dza� kodem �r�d�owym opracowywanym
przez nawet bardzo du�e zesp�y programist�w umo�liwiaj�c �ledzenie i
kontrol� wszystkich zmian w trakcie pracy nad projektami i wypuszczaniem
pe�nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya toplulu�unun
s�r�m denetimini, denetimi yap�lm�� dizinlerin hiyerar�ik toplulu�una
geni�leten rcs(1) s�r�m denetim sisteminin �n y�z�d�r. Bu dizin ve
dosyalar, bir yaz�l�m yay�n� olu�turma amac�yla biraraya getirilebilir.
CVS, bu yaz�l�m yay�nlar�n�n y�netilmesini ve kaynak dosyalar� bak�m�n�n
birden �ok yaz�l�m geli�tiricisi taraf�ndan e�zamanl� olarak yap�lmas�n�
kontrol etmek i�in gereken i�levleri sa�lar.

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
