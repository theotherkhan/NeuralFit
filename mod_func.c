#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _K1_reg(void);
extern void _leak_reg(void);
extern void _Na_T_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," K1.mod");
    fprintf(stderr," leak.mod");
    fprintf(stderr," Na_T.mod");
    fprintf(stderr, "\n");
  }
  _K1_reg();
  _leak_reg();
  _Na_T_reg();
}
