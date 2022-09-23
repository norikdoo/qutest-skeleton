#include <stdint.h>
#include "skeleton.h"
#include "qpc.h"

Q_DEFINE_THIS_MODULE("SKELETON")

/* Public variables to demonstrate poke() */
int skeleton_value = 0;

int SKELETON_init(uint32_t param)
{
    /* Assertions */
    Q_ASSERT(param < SKELETON_PARAM_MAX);

    /* Return skeleton_value if changed by poke() */
    if (skeleton_value != 0)
        return skeleton_value;

    /* Some implementation here */
    if (param > 5)
        return param;
    else
        return 0;
}
