"""new content column

Revision ID: b3c43216c65d
Revises: cdec995ccb78
Create Date: 2024-10-16 21:17:09.618907

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c43216c65d'
down_revision: Union[str, None] = 'cdec995ccb78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
