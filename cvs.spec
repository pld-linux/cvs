Summary:     Concurrent Versioning System
Summary(de): Concurrent-Versioning-System
Summary(fr): CVS : Concurrent Versioning System
Summary(pl): Concurrent Versioning System
Summary(tr): Sürüm denetim sistemi
Name:        cvs
Version:     1.10.3
Release:     2
Copyright:   GPL
Group:       Development/Version Control
Source0:     http://download.cyclic.com/pub/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch:       cvs-tmprace.patch
URL:         http://www.cyclic.com/
Prereq:      /sbin/install-info
Buildroot:   /tmp/%{name}-%{version}-root

%description
CVS is a front end to the rcs(1) revision control system which extends the
notion of revision control from a collection of files in a single directory
to a hierarchical collection of directories consisting of revision
controlled files.  These directories and files can be combined together to
form a software release.  CVS provides the functions necessary to manage
these software releases and to control the concurrent editing of source
files among multiple software developers.

%description -l de
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den Begriff
der Revisionskontrolle von einer Sammlung von Dateien in einem " "einzelnen
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
pomoc± CVS w ³atwy sposób mo¿na zarz±dzaæ kodem ¼ród³owym opracowywany przez
nawet bardzo du¿e zespó³y programistów umo¿liwiaj±c ¶ledzenie i kontrolê
wszystkich zmian w trakcie pracy nad projektami i wypuszczaniem pe³nych
wersji oprogramowania (releas).

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
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure \
	--prefix=/usr \
	--enable-server \
	--enable-client
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr
make install-info prefix=$RPM_BUILD_ROOT/usr
gzip -9nf $RPM_BUILD_ROOT/usr/info/cvs*

strip $RPM_BUILD_ROOT/usr/bin/cvs

%post
/sbin/install-info /usr/info/cvs.info.gz /usr/info/dir --entry="* cvs: (cvs).          A version control system for multiple developers."
/sbin/install-info /usr/info/cvsclient.info.gz /usr/info/dir --entry="* cvsclient: (cvsclient).                       The CVS client/server protocol."

%preun
if [ $1 = 0 ]; then
	/sbin/install-info --delete /usr/info/cvs.info.gz /usr/info/dir --entry="* cvs: (cvs).		A version control system for multiple developers."
	/sbin/install-info --delete /usr/info/cvsclient.info.gz /usr/info/dir --entry="* cvsclient: (cvsclient).                       The CVS client/server protocol."
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog doc/*.ps
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man[158]/*
/usr/info/cvs*
%attr(  -, root, root) /usr/lib/cvs

%changelog
* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.1-2]
- fix race conditions in cvsbug/rcs2log.

* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.10.1-1]
- removed "Requires: rcs",
- added fixed rcs2log.sh script.

* Sat Aug  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9.29-1]
- added pl translation,
- added -q %setup parametr,
- added URL,
- Changed Source url,
- spec file rewritten for using Buildroot,
- added ChangeLog to %doc,
- added %clean section,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added install-info stuff
- added changelog section
